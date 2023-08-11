import { Avatar, Box, Icon, Skeleton, Text, Menu, MenuButton, MenuList, MenuItem, Flex} from '@chakra-ui/react'
import React from 'react'
import { useProfile } from '../../api/auth/useProfile'
import { IoChevronDown, IoSearch, IoStorefront } from 'react-icons/io5'
import useLogout from '../../api/auth/useLogout';
import FormikInput from '../forms/FormikInput';
import { Formik } from 'formik';
import { Link, useLocation } from 'react-router-dom';

function Header() {

    const {data, isLoading} = useProfile();
    const {mutate} = useLogout()


    return (
        <Box w='full'>
            <Flex borderRadius='2xl' bgColor='white' p='3' display='flex' alignItems='center' justifyContent='space-between' px='8'>
                <Flex gap={4} >
                    <Menu >
                        <MenuButton _hover={{bgColor: "gray.50", }} p='1' borderRadius="500rem">
                            <Flex alignItems='center' gap='5'>
                                <Flex w='40px' h='40px' borderRadius='full' bgColor='gray.100' alignItems='center' justifyContent='center'>
                                    <Icon fontSize='xl' color='gray.600' as={IoStorefront}></Icon>
                                </Flex>
                                <Text fontWeight='semibold'>Autoescuelas ECO</Text>
                                <Icon as={IoChevronDown} color='gray.400'></Icon>
                            </Flex>
                        </MenuButton>

                        <MenuList>
                            <MenuItem color='red.500' onClick={() => mutate()}>Log Out</MenuItem>
                        </MenuList>
                    </Menu>
                </Flex>
                <Menu>
                    <MenuButton>
                        <Box display='flex' alignItems='center' gap='3'>
                            <Avatar name='Jose Peña' w='40px' h='40px'>
                            </Avatar>
                                    <Box cursor='pointer'>
                                        <Text fontSize='md' fontWeight='semibold' color='gray.800'>
                                            {data?.first_name} {data?.last_name}
                                        </Text>
                                        <Text fontSize='xs' fontWeight='regular' color='gray.500'>
                                            {data?.email}
                                        </Text>
                                    </Box>
                                    <Icon as={IoChevronDown} color='gray.400'></Icon>

                        </Box>
                    </MenuButton>
                    <MenuList>
                        <MenuItem color='red.500' onClick={() => mutate()}>Log Out</MenuItem>
                    </MenuList>
                </Menu>
            </Flex>
        </Box>
        
    )
}

export default Header
