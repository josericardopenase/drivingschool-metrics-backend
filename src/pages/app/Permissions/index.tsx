import React, { Suspense } from 'react'
import useLogout from '../../../api/auth/useLogout'
import Graph1 from '../../../components/charts/Chart1'
import { Text, Box, Container, SimpleGrid } from '@chakra-ui/react'
import Chart1 from '../../../components/charts/Chart1'

interface Props {}

function Permissions(props: Props) {
    return (
        <>
            <Text fontSize='3xl' fontWeight='semibold' mb='3'>Permisos</Text>
            <SimpleGrid columns={2} mt='10'>
                    <Chart1/>
            </SimpleGrid>
        </>
    )
}
export default Permissions
