
import axios, { AxiosRequestConfig, InternalAxiosRequestConfig } from 'axios';
import qs from 'qs'

const APIClient = axios.create({
    baseURL: import.meta.env.VITE_API,
    paramsSerializer: params => {
        // all params that are array must be handled like a string with comma separation
        // must implement default serializer for the other params
        return qs.stringify(params, { arrayFormat: 'comma' })
      }
})

function  getTokenInterceptor(config : AxiosRequestConfig) : InternalAxiosRequestConfig{
    const token = localStorage.getItem('token');
    if (token) {
        config.headers = {
            ...config.headers,
            Authorization: `Token ${token}`,
          };
    }
    return config as InternalAxiosRequestConfig;
}

APIClient.interceptors.request.use(getTokenInterceptor);

export default APIClient
