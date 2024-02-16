import React from 'react'
import { Text, SimpleGrid } from '@chakra-ui/react'
import Chart1 from '../../../components/charts/Chart1'
import Chart4 from '../../../components/charts/Chart4'
import { useProfile } from '../../../api/auth/useProfile'

interface Props {}

function Dashboard(props: Props) {

    const profile = useProfile()

    return (
        <>
            <Text fontSize='3xl' fontWeight='semibold' mb='3'>General</Text>
            <SimpleGrid columns={1} mt='5' gap='4'>
                {
                    profile.data?.driving_school &&
                    <>
                        <Chart1 drivingSchoolId={profile.data?.driving_school}></Chart1>
                        <Chart4 drivingSchoolId={profile.data?.driving_school}></Chart4>
                    </>
                }
            </SimpleGrid>
        </>
    )
}
export default Dashboard
