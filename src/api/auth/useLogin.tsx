import {useMutation, UseMutationOptions} from 'react-query'
import APIClient from '../client';

export async function login(username: string, password: string) {
    try {
      const response = await APIClient.post('/auth/token/', {
        username,
        password,
      });
      localStorage.setItem('token', response.data.token)
      return response.data; // Assuming the API returns a token on successful login
    } catch (error) {
      throw new Error('Authentication failed. Please check your credentials.');
    }
  }
  

export const useLogin =  (settings? : Omit<UseMutationOptions<any, unknown, unknown, any>, "mutationFn"> ) =>  useMutation((formData: { username: string; password: string }) => login(formData.username, formData.password), settings );