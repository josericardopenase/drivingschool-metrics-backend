import { Box, Center, Flex, Icon, SimpleGrid, Text, Image } from '@chakra-ui/react'
import { Formik, replace } from 'formik'
import React from 'react'
import FormikInput from '../../../components/forms/FormikInput'
import FormikButton from '../../../components/forms/FormikButton'
import {IoMdMail, IoMdLock} from 'react-icons/io'
import { useLogin } from '../../../api/auth/useLogin'
import { useNavigate } from 'react-router-dom'
import logo from '../../../assets/logo.png'
import charts from '../../../assets/graphs.png'

interface Props {}

function Login(props: Props) {

    const navigate = useNavigate()
    const {mutate, error, isLoading} = useLogin({
        onSuccess: () => navigate("/", {replace: true}) 
    })

    return (
        <SimpleGrid columns={2} bgColor='gray.100' height='100vh' backgroundColor='primary.500' p='4'>
                <Image  src={"https://www.autoescuelaseco.com/wp-content/uploads/2023/07/new-logo.png"} position='absolute' w='200px' p='10'></Image>
                <Center bgColor='white' w='100%' p="12" shadow='lg-soft' borderRadius='3xl' display='flex' gap={8} flexDir='column'>
                    <Box w='100%' maxW='540px' flexDir='column' display='flex' gap='7'>
                        <Box>
                            <Text fontSize='3xl' color='gray.800' fontWeight='bold'>Iniciar Sesión</Text>
                            <Text fontSize='lg' color='gray.500' mt='1'>Usa tu email y tu contraseña</Text>
                        </Box>
                        <Formik initialValues={{username : "", password: ""}} onSubmit={(data) => {mutate(data)}}>
                            {
                                () => (
                                    <Flex flexDir='column' gap={5}>
                                        <FormikInput  size='md' borderRadius='3xl' iconLeft={IoMdMail}  label='Email' variant='filled' placeholder='jhon@doe.com' name='username'></FormikInput>
                                        <FormikInput size='md'  type='password' borderRadius='3xl'  iconLeft={IoMdLock} label='Password' variant='filled' placeholder='Password' name='password'></FormikInput>
                                        <FormikButton borderRadius='3xl' isLoading={isLoading} size='md' colorScheme='primary'>Login</FormikButton>
                                        <Text  color='red.500'>{error?.toString()}</Text>
                                    </Flex>
                                )
                            }
                        </Formik>
                    </Box>
                </Center>
                <Center>
                    <Box textAlign='center'>
                        <Text color='white' fontWeight='bold' fontSize='3xl'>Tu Autoescuela en números</Text>
                        <Text color='whiteAlpha.700' fontWeight='semibold' fontSize='xl'>Mide hasta el mínimo detalle con datos oficiales de la DGT</Text>
                        <Image  src={"https://www.autoescuelaseco.com/wp-content/uploads/2021/04/foto-coches.jpg"} w='680px' p='6' borderRadius="50px"></Image>
                    </Box>
                </Center>
        </SimpleGrid>
    )
}

export default Login
