import React from 'react'
import { Text, SimpleGrid } from '@chakra-ui/react'
import Chart1 from '../../../components/charts/Chart1'
import Chart4 from '../../../components/charts/Chart4'

interface Props {}

function Dashboard(props: Props) {

    return (
        <>
            <Text fontSize='3xl' fontWeight='semibold' mb='3'>General</Text>
            <SimpleGrid columns={1} mt='5' gap='4'>
                <Chart1></Chart1>
                <Chart4></Chart4>
            </SimpleGrid>
        </>
    )
}
export default Dashboard
