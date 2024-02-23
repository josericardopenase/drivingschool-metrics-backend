import React, { Suspense, useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Text } from 'recharts';
import BaseChart from './BaseChart';
import FormikApiSelect from '../forms/FormikApiSelect';
import { useGraphData } from '../../api/metrics/graph1';
import { months } from '../../utils/dates';
import { DrivingSchoolService } from '../../api/resources/driving/schools';
import { Box, Flex } from '@chakra-ui/react';
import FormikSelect from '../forms/FormikSelect';
import FormikMultipleSelect from '../forms/FormikMultipleSelect';
import { PermissionServices } from '../../api/resources/driving/permissions';
import { TestTypeService } from '../../api/resources/tests/types';
import { DrivingSchoolSectionsService } from '../../api/resources/driving/schoolsSections';

const pallete =[
  '#D53F8C',
  '#6B46C1',
  '#67AAF9',
  '#44337A',
  '#322659',
];
const generateCustomColor = (index : number) => {
  return pallete[index % pallete.length];
};


export default function Chart4({sections} : {sections : number[]}){

  const [filters, setFilters] = useState({year: "2023", section: sections })
  const {data, isLoading} = useGraphData('graph3', filters);

    return (
      <BaseChart setFilters={setFilters} filtersValue={filters} title='Comparativa por año' filters={<Flex gap={3} alignItems='center' justifyContent='space-between'>
        <FormikApiSelect apiService={DrivingSchoolSectionsService} label="Secciones de autoescuelas" name='section'>
          {
            (x) => <Box><Text>{x.name}</Text></Box>
          }
        </FormikApiSelect>
        <Flex alignItems='center' gap={2}>
          <FormikApiSelect single apiService={TestTypeService} label="Tipo de examen" name='test_type'>
            {
              (x) => <Box><Text>{x.name}</Text></Box>
            }
          </FormikApiSelect>
          <FormikApiSelect single apiService={PermissionServices} label="Permisos" name='permission'>
            {
              (x) => <Box><Text>{x.name}</Text></Box>
            }
          </FormikApiSelect>
          <FormikSelect variant='filled' w='fit-content' name='metrica' options={[{label: "Presentados", value: "num_presentados"}, {label: "Suspensos", value: "num_suspensos"}, {label: "Aprobados", value: "num_aptos"}, {label: "Aprobados 1 conv", value: "num_aptos_1_conv"}, ]}></FormikSelect >
          <FormikSelect variant='filled' w='fit-content' name='year' options={[{label: "2025", value: "2025"}, {label: "2024", value: "2024"}, {label: "2023", value: "2023"}, {label: "2022", value: "2022"}, {label: "2021", value: "2021"}, {label: "2020", value: "2020"}, ]}></FormikSelect>
        </Flex>
      </Flex>}>
        <ResponsiveContainer width="100%" height={380}>
          <LineChart
          height={500}
            data={data?.records}
            margin={{
              top: 5,
              right: 10,
              left: -10,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={data?.info.x_label} tickFormatter={(x) => months[x-1]} />
            <YAxis />
            <Tooltip />
            <Legend />
            {
              data?.info.y_labels.map((x, i) => 
                <Line strokeWidth={3} type="monotone" dataKey={x} activeDot={{ r: 8 }}  stroke={generateCustomColor(i)} />
              )
            }
          </LineChart>
        </ResponsiveContainer>
    </BaseChart>
    );
}