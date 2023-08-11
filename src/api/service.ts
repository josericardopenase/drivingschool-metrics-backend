import { Plank } from "../engines/http-plank/src/core/client";
import { ApiError } from "../engines/http-plank/src/types/error";
import APIClient from "./client";

export const service = new Plank<ApiError>(APIClient);