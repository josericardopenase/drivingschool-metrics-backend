import {useMutation, UseMutationOptions} from 'react-query'
import APIClient from '../client';
import { useNavigate } from 'react-router-dom';

export default function useLogout(){

    const navigate = useNavigate();

    function mutate(){
        localStorage.removeItem('token')
        navigate('/login')
    }

    return {mutate}

}