import React from 'react'
import { useProfile } from '../../api/auth/useProfile'
import { Outlet } from 'react-router-dom'
import { Box } from '@chakra-ui/react'
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'

function AppContainer() {
    return (
        <Box minH='100vh' bgColor='gray.100'>
            <Sidebar></Sidebar>
            <Box ml='290px' position='relative' h='100vh' p='3' overflow='hidden' display='flex' flexDir='column' alignItems='stretch' gap={3}>
                <Header/>
                <Box h='full' overflow='auto'  p='5'>
                    <Outlet></Outlet>
                </Box>
            </Box>
        </Box>
    )
}

export default AppContainer
