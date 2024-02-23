import React, { Suspense, useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Text } from 'recharts';
import BaseChart from './BaseChart';
import FormikApiSelect from '../forms/FormikApiSelect';
import { useGraphData } from '../../api/metrics/graph1';
import { months } from '../../utils/dates';
import { DrivingSchoolPermission } from '../../api/resources/driving/permissions';

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


export default function PermissionChart({permission, year, drivingSchools, test_type, metrica } : { metrica : string, drivingSchoolId :number, permission: DrivingSchoolPermission, year : string, drivingSchools : number[], test_type : undefined | number}){

  const {data, isLoading, isError, status, isRefetching, isRefetchError} = useGraphData('graph1', {year: year, autoescuela: drivingSchools, permission: permission.id, test_type : test_type, metrica : metrica});

    if(isError || isRefetching || isRefetchError || status === "loading") return <></>

    return (
      <BaseChart setFilters={() => {}} filtersValue={{}} title={"Permiso " + permission.name} filters={<></>}>
        <ResponsiveContainer width="100%" height={380}>
          <LineChart
          height={500}
            data={data?.records.sort((x, y) => x.month - y.month)}
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