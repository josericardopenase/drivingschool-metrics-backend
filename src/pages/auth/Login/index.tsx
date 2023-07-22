import { Box, Center, Flex, Text } from '@chakra-ui/react'
import { Formik, replace } from 'formik'
import React from 'react'
import FormikInput from '../../../components/forms/FormikInput'
import FormikButton from '../../../components/forms/FormikButton'
import {IoMdMail, IoMdLock} from 'react-icons/io'
import { useLogin } from '../../../api/auth/useLogin'
import { useNavigate } from 'react-router-dom'

interface Props {}

function Login(props: Props) {

    const navigate = useNavigate()
    const {mutate, error, isLoading} = useLogin({
        onSuccess: () => navigate("/dashboard", {replace: true}) 
    })
console.log(error)
    return (
        <Center bgColor='gray.100' height='100vh'>
                <Box bgColor='white' maxW='450px' w='100%' p="12" shadow='md' borderRadius='2xl' display='flex' gap={8} flexDir='column'>
                    <Box>
                        <Text fontSize='2xl' color='gray.800' fontWeight='bold'>Iniciar Sesión</Text>
                        <Text fontSize='lg' color='gray.500' mt='1'>Usa tu email y tu contraseña</Text>
                    </Box>
                    <Formik initialValues={{username : "", password: ""}} onSubmit={(data) => {mutate(data)}}>
                        {
                            () => (
                                <Flex flexDir='column' gap={5}>
                                    <FormikInput borderRadius='xl' iconLeft={IoMdMail} label='Email' variant='filled' placeholder='jhon@doe.com' name='username'></FormikInput>
                                    <FormikInput  type='password' borderRadius='xl' iconLeft={IoMdLock} label='Password' variant='filled' placeholder='Password' name='password'></FormikInput>
                                    <FormikButton isLoading={isLoading} borderRadius='xl' colorScheme='red'>Login</FormikButton>
                                    <Text color='red.500'>{error?.toString()}</Text>
                                </Flex>
                            )
                        }
                    </Formik>
                </Box>
        </Center>
    )
}

export default Login
