import { UseBaseQueryOptions, UseMutationOptions, UseQueryOptions } from "react-query/types/react/types"

export type mutateOptions<TData, TError = unknown, TVariables = unknown, TContext = unknown> = UseMutationOptions<TData, TError, TVariables, TContext>
export type queryOptions<TData, TError = unknown, TVariables = unknown> = UseQueryOptions<TData, TError, TVariables>

export interface configurations extends UseBaseQueryOptions {
	optimisticUpdates?: boolean
	refetchInterval?: number
	pageSize?: number
	pk?: any
}

export interface listApiResponse<Type> {
	results: Type[]
	next?: number
	previous?: number
}
