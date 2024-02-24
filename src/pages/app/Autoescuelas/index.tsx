import React, { Suspense } from 'react'
import { Text, Box, Container, SimpleGrid } from '@chakra-ui/react'
import Chart1 from '../../../components/charts/Chart1'
import Chart3 from '../../../components/charts/Chart3'
import { useProfile } from '../../../api/auth/useProfile'
import { DrivingSchoolSectionsService } from '../../../api/resources/driving/schoolsSections'
import MorePresentedsDrivingSchool from '../../../components/charts/MorePresentedsDrivingSchool'

interface Props {}

function Autoescuelas(props: Props) {

    const profile = useProfile()
    const sections = DrivingSchoolSectionsService.useList({driving_school__id : profile.data?.driving_school})

    return (
        <>
            <Text fontSize='3xl' fontWeight='semibold' mb='3'>Permisos</Text>
            <SimpleGrid mt='10'>
                <MorePresentedsDrivingSchool></MorePresentedsDrivingSchool>
            </SimpleGrid>
        </>
    )
}
export default Autoescuelas
