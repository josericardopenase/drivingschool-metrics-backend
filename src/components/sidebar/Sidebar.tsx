import { Box, Icon, Text, Image } from '@chakra-ui/react'
import { BiHome, BiWallet, BiStore  } from 'react-icons/bi'
import React from 'react'
import { Link, useLocation } from 'react-router-dom';
import logo from '../../assets/logopositive.png'
import { IconType } from 'react-icons';

interface Props {
    to: string,
    children: React.ReactNode
    icon: IconType
}

function HeaderLink({ to, children, icon }: Props) {
    const location = useLocation();
    const isActive = location.pathname === to;
  
    return (
      <Link to={to}>
        <Box
        _hover={{bgColor: "whiteAlpha.300"}}
        bgColor={isActive ? "whiteAlpha.400" : undefined}
          color={'white'}
          fontWeight='medium'
          cursor='pointer'
          borderRadius='500rem'
          display='flex'
          alignItems='center'
          gap={2}
          px='3'
          py='2'
        >
           
            <Icon fontSize='2xl' as={icon}></Icon>
        <Text>
          {children}
        </Text>
        </Box>
      </Link>
    );
  }
function Sidebar() {

    return (
        <Box position='fixed' left='0' h='100vh' zIndex='10' p='2' display='flex' justifyContent='space-between' w='300px' >
           <Box h='100%' bgColor='primary.500' borderRadius='3xl' p='6' w='100%' display='flex' flexDirection='column' gap={14} shadow='xl'>
                <Box>
                    <Image w='150px' src={logo}></Image>
                </Box>
                <Box gap={6} display='flex' flexDir='column'>
                    <HeaderLink icon={BiHome} to='/'>General</HeaderLink>
                    <HeaderLink icon={BiWallet} to='/permissions'>Permisos</HeaderLink>
                    <HeaderLink icon={BiStore} to='/sections'>Secciones</HeaderLink>
                </Box>
            </Box>
        </Box>
    )
}

export default Sidebar
