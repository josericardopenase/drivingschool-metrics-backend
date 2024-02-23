import { AxiosError, AxiosInstance } from "axios";
import { configurations, listApiResponse } from "../types/apitypes";
import {  QueryFunctionContext, useInfiniteQuery, useMutation, useQuery } from "react-query";

export class ApiService<Type, ErrorType, PaginatedType>{
    private client : AxiosInstance;
    private queryKeys : string[];
    private url : string;
    protected config ?: configurations;


    public constructor(client : AxiosInstance, queryKeys : string[] | string, url : string, config ?: configurations){
        this.client = client;
        this.queryKeys = typeof queryKeys === "string" ? [queryKeys] : queryKeys;
        this.url = url;
        this.config = config;
    }

    public get useRetrieve() {
        return (id: number, config?: configurations) =>
          useQuery<Type, AxiosError<ErrorType>>([...this.queryKeys, 'retrieve', id], async () => {
              const response = await this.client.get<Type>(`${this.url}${id}/`);
              return response.data;
          }, 
          {
            ...this.config as any,
            ...config as any
          });
      }
    public get useList(){
        return (filters : any = {}, config : configurations = {}) => 
        useQuery<PaginatedType, AxiosError<ErrorType>>([...this.queryKeys, 'list', filters], async () => {
            const response = await this.client.get<PaginatedType>(this.url, {params: filters})
            return response.data;
        },
        {
          retry: 0,
          refetchOnReconnect: false,
          refetchOnWindowFocus: false
        }
       )
    }

    public get useInfiniteList() {
        return (
          filters: any = {},
          config: configurations = {}
        ) =>
          useInfiniteQuery<PaginatedType, AxiosError<ErrorType, any>>(
            [...this.queryKeys, 'infinite-list', filters],
            async (context: QueryFunctionContext<any>) => {
              const response = await this.client.get<PaginatedType>(this.url, { params: { 
                page_size: this.config?.pageSize ?? 20,
                page: context.pageParam, 
                ...filters,  } });
              return response.data;
            },
            {
              ...this.config as any,
              ...config as any,
              keepPreviousData: true,
              getNextPageParam: (lastPage : any) => lastPage.next,
              getPreviousPageParam: (firstPage : any) => firstPage.previous,
            }
          );
      }

    public get useCreate() {
        return () => useMutation<Type, AxiosError<ErrorType>, Omit<Type, 'id'>>(
          async (newItem: Omit<Type, 'id'>) => {
            const response = await this.client.post<Type>(`${this.url}`, newItem);
            return response.data;
          },
          {
            ...this.config as any,
          }
        );
    }

    public useUpdate() {
        return useMutation<Type, AxiosError<ErrorType>, Partial<Type>>(
          async (updatedItem: Partial<Type>) => {
            // Replace 'id' below with the actual identifier for the resource to be updated
            //this is throwing error Element implicitly has an 'any' type because expression of type 'any' can't be used to index type 'Partial<Type>
            const id = (updatedItem as any)[this.config?.pk ?? 'id'];

            if (!id) {
              throw new Error('Missing identifier for the resource to be updated.');
            }
    
            const response = await this.client.put<Type>(`${this.url}${id}/`, updatedItem);
            return response.data;
          },
          {
            ...this.config as any,
          }
        );
      }


    public useDestroy() {
        return useMutation<Type, AxiosError<ErrorType>, number>(
        async (id: number) => {
            const response = await this.client.delete(`${this.url}${id}/`);
            return response.data;
        },
        {
            ...this.config as any,
        }
        );
    }
}

export class Plank<ErrorType>{
    private APIClient : AxiosInstance;

    public constructor(client : AxiosInstance){
        this.APIClient = client;
    }

    public createService<Type extends {id ?: number | string}>(queryKeys : string[] | string, url : string, config ?: configurations ){
        //return new ApiService();
        return new ApiService<Type, ErrorType, listApiResponse<Type>>(this.APIClient, queryKeys, url, config);
    }
}

