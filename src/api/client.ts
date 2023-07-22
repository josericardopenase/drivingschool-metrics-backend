
import axios, { AxiosInstance, AxiosRequestConfig, InternalAxiosRequestConfig } from 'axios';


const APIClient = axios.create({
    baseURL: "http://127.0.0.1:8000/"
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
