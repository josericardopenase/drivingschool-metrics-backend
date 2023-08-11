import { Chart } from '../../types/db/chart';
import APIClient from '../client';
import { useQuery } from 'react-query';

async function getGraphData(filters :  any, chart : string) {
  try {
    const response = await APIClient.get(`/metrics/${chart}/`, {
      params: filters,
    });
    return response.data;
  } catch (error) {
    throw new Error('Error fetching graph data');
  }
}
export function useGraphData(chart: string, filters : any) {
  return useQuery<Chart, Error, Chart, any>(['graphData', filters], () => getGraphData(filters, chart));
}


