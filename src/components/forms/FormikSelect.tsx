import { Flex, Icon, Input, InputGroup, InputLeftElement, InputProps, InputRightElement, Select, SelectProps, Text } from '@chakra-ui/react'
import React from 'react'
import { useField } from 'formik';
import { IconType } from 'react-icons'

interface Props extends SelectProps {
    name : string
    label ?: string
    iconLeft ?: IconType
    iconRight ?: IconType
    options: {value: string, label : string}[]
}

function FormikSelect({name, label, iconLeft, iconRight, options, ...props}: Props) {

    const [field, meta, helpers] = useField(name);
    const isInvalid = (meta.error?.length ?? 0) > 0

    return (
        <Flex flexDir='column' gap='2' p='1'>
            { label && <Text color='gray.500'>{label}</Text> }
            <InputGroup >
            {
                iconLeft &&
                <InputLeftElement  color='gray.500' pointerEvents='none'>
                    <Icon fontSize='xl' as={iconLeft}></Icon>
                </InputLeftElement>
            }
            <Select py='4'isInvalid={isInvalid} {...props} {...field}>
                {
                    options.map((x) => <option value={x.value}>{x.label}</option>)
                }
            </Select>
            {
                iconRight && 
                <InputRightElement  pointerEvents='none' color='gray.500'>
                    <Icon as={iconRight}></Icon>
                </InputRightElement>
            }
            </InputGroup>
        </Flex>
    )
}

export default FormikSelect
