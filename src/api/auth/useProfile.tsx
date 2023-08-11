import { useQuery, UseQueryOptions } from 'react-query';
import APIClient from '../client';
import { User } from '../../types/db/user';

async function fetchUserProfile(): Promise<User> {
  const response = await APIClient.get('/auth/profile/');
  return response.data;
}

export const useProfile = (settings?: UseQueryOptions<User>) => {
  return useQuery<User>('profile', fetchUserProfile, settings);
};
