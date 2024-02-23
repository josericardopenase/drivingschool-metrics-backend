import React from 'react'
import { Text, SimpleGrid, Box, Center, Icon } from '@chakra-ui/react'
import Chart1 from '../../../components/charts/Chart1'
import Chart4 from '../../../components/charts/Chart4'
import { useProfile } from '../../../api/auth/useProfile'
import { FaStore } from 'react-icons/fa'

interface Props {}

function Dashboard(props: Props) {

    const profile = useProfile()

    return (
        <>
            <Text fontSize='3xl' fontWeight='semibold' mb='3'>General</Text>
            <SimpleGrid columns={1} mt='5' gap='4'>
                {
                    profile.data?.driving_school ?
                    <>
                        <Chart1 drivingSchoolId={profile.data?.driving_school}></Chart1>
                        <Chart4 drivingSchoolId={profile.data?.driving_school}></Chart4>
                    </>
                    :
                    <Center flexDir="column"  mt="40">
                        <Center width="250px" height='250px' color="gray.700" backgroundColor='white' borderRadius="50%">
                            <Icon fontSize="120px" as={FaStore}></Icon>
                        </Center>
                        <Text mt="5" fontSize="30px" fontWeight="semibold">Lo sentimos...</Text>
                        <Text color="gray.500" >No tienes ninguna autoescuela asociada</Text>
                    </Center>
                }
            </SimpleGrid>
        </>
    )
}
export default Dashboard
