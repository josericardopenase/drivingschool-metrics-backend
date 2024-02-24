import React from 'react'
import { useGraphData } from '../../api/metrics/graph1'
import { Box, Flex, Text } from '@chakra-ui/react';
import { Bar, BarChart, CartesianGrid, Legend, Rectangle, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

interface Props {}

function MorePresentedsDrivingSchool(props: Props) {
  const {data, isLoading} = useGraphData('more_presenteds', {});

    return (
        <Box backgroundColor="white" p="4" borderRadius="xl">
            <Text fontSize="20px" fontWeight="semibold">Autoescuelas con mas presentados</Text>
            <Box height="400px" mt="4">
            <ResponsiveContainer width="100%" height="100%">
                <BarChart
                width={500}
                height={300}
                data={data?.records.filter((x, y)=> y < 13).map((x) => ({
                    ...x,
                    autoescuela: x.autoescuela.toLowerCase().replace("autoescuelas", "").replace("autoescuela", ""),
                }))}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                }}
                >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="autoescuela" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="total_presentados" fill="#8884d8" />
                </BarChart>
            </ResponsiveContainer>
            </Box>
            <Box maxH="400px" overflow="auto" mt="3">
                <>
                {
                            data?.records.map((x)=> (
                                <Flex justifyContent="space-between">
                                    <Text fontWeight="semibold">{x.autoescuela}</Text>
                                    <Text fontWeight="semibold" color="gray.600">{x.total_presentados}</Text>
                                </Flex>
                            ))
                }
                </>
            </Box>
        </Box> 
    )
}

export default MorePresentedsDrivingSchool
