import React, { useState } from 'react'
import {
    Menu,
    MenuButton,
    MenuList,
    MenuItemOption,
    Button,
    Input,
    Box,
    Icon,
    Flex,
  } from '@chakra-ui/react'
import { useField } from 'formik';
import { IoCheckmark, IoChevronDown } from 'react-icons/io5'
import { ApiService } from '../../engines/http-plank/src/core/client';
import { listApiResponse } from '../../engines/http-plank/src/types/apitypes';

interface Props<T extends {id ?: number}> {
    label : React.ReactNode | string,
    name : string,
    options: {value: string, label : string}[]
}

function FormikMultipleSelect<T extends {id ?: number}>(props: Props<T>) {

    const [text, setText] = useState("");

    const [field, meta, helpers] = useField(props.name);

    function toggleValue(id :any){
      if(field.value.includes(id)){
        helpers.setValue(field.value.filter((x : any) => x != id));
      }else{
        helpers.setValue([...field.value, id]);
      }
    }


    return (
        <Menu closeOnSelect={false}>
        <MenuButton rightIcon={<Icon as={IoChevronDown}></Icon>} as={Button} colorScheme='gray'>
          {
            props.label
          }
        </MenuButton>
        <MenuList  minWidth='240px' scrollBehavior='smooth'>
            <Box p='2'>
                <Input size='sm' placeholder='search...' onChange={(e) => setText(e.target.value)}></Input>
           </Box>
          <Box defaultValue='asc' title='Order'  overflow='auto' maxH='200px'>
            {
              props.options?.map((x) => 
                  <Flex cursor='pointer' alignItems='center' px='4' py='1' onClick={() => {toggleValue(x.value ?? 0)}}>
                    
                    {
                      field.value.includes(x.value) ? <Icon color='green.500' as={IoCheckmark}></Icon> : null
                    }
                    {x.label}
                  </Flex>
              )

            }
          </Box>
        </MenuList>
      </Menu>    
    )
}

export default FormikMultipleSelect
