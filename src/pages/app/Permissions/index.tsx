import React, { Suspense, useState } from 'react'
import useLogout from '../../../api/auth/useLogout'
import Graph1 from '../../../components/charts/Chart1'
import { Text, Box, Container, SimpleGrid, Flex } from '@chakra-ui/react'
import Chart1 from '../../../components/charts/Chart1'
import { TestTypeService } from '../../../api/resources/tests/types'
import { PermissionServices } from '../../../api/resources/driving/permissions'
import PermissionChart from '../../../components/charts/PermissionChart'
import { useProfile } from '../../../api/auth/useProfile'
import FormikApiSelect from '../../../components/forms/FormikApiSelect'
import FormikSelect from '../../../components/forms/FormikSelect'
import { DrivingSchoolService } from '../../../api/resources/driving/schools'
import BaseForm from '../../../components/charts/BaseForm'

interface Props {}

function Permissions(props: Props) {
    const profile = useProfile();
    const tests = TestTypeService.useList();
    const permission = PermissionServices.useList({}, 
        {retry: 1, retryDelay: 3000, retryOnMount: false, refetchOnReconnect: false, refetchOnWindowFocus: false, refetchIntervalInBackground: false}
        );

    const [filters, setFilters] = useState({year: "2023", autoescuela: []});
    

    return (
        <>
        <Text fontSize='3xl' fontWeight='semibold' mb='3'>Permisos</Text>
        <BaseForm setFilters={setFilters} filtersValue={filters}
        filters={
            <Flex gap={3} alignItems='center' justifyContent='space-between' backgroundColor="white" px="4" borderRadius="9">
                <Flex gap={3}>
                    <FormikApiSelect apiService={DrivingSchoolService} label="Autoescuelas" name='autoescuela'>
                    {
                        (x) => <Box><Text>{x.name}</Text></Box>
                    }
                    </FormikApiSelect>
                    <FormikApiSelect single apiService={TestTypeService} label="Tipo de examen" name='test_type'>
                        {
                        (x) => <Box><Text>{x.name}</Text></Box>
                        }
                    </FormikApiSelect>
                </Flex>
                <Flex alignItems='center' gap={2}>
                <FormikSelect variant='filled' w='fit-content' name='metrica' options={[{label: "Presentados", value: "num_presentados"}, {label: "Suspensos", value: "num_suspensos"}, {label: "Aprobados", value: "num_aptos"}, {label: "Aprobados 1 conv", value: "num_aptos_1_conv"}, ]}></FormikSelect>
                <FormikSelect variant='filled' w='fit-content' name='year' options={[{label: "2025", value: "2025"}, {label: "2024", value: "2024"}, {label: "2023", value: "2023"}, {label: "2022", value: "2022"}, {label: "2021", value: "2021"}, {label: "2020", value: "2020"}, ]}></FormikSelect>
                </Flex>
            </Flex>

        }>
            <SimpleGrid columns={2} mt='10' gap={4}>
                {
                    profile.data?.driving_school &&
                        permission?.data?.results.map(x => (
                            <PermissionChart metrica={(filters as any).metrica} test_type={(filters as any).test_type} year={filters.year} drivingSchools={[profile.data.driving_school, ...filters.autoescuela]} drivingSchoolId={profile.data?.driving_school} permission={x}></PermissionChart>
                        ))
                }
            </SimpleGrid>
        </BaseForm>
        </>
    )
}
export default Permissions
