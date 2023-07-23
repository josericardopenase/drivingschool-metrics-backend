import { Flex, Icon, Input, InputGroup, InputLeftElement, InputProps, InputRightElement, Text } from '@chakra-ui/react'
import React from 'react'
import { useField } from 'formik';
import { IconType } from 'react-icons'

interface Props extends InputProps {
    name : string
    label ?: string
    iconLeft ?: IconType
    iconRight ?: IconType
}

function FormikInput({name, label, iconLeft, iconRight, ...props}: Props) {

    const [field, meta, helpers] = useField(name);
    const isInvalid = (meta.error?.length ?? 0) > 0

    return (
        <Flex flexDir='column' gap='2' p='1'>
            { label && <Text color='gray.500'>{label}</Text> }
            <InputGroup {...props}>
            {
                iconLeft &&
                <InputLeftElement  color='gray.500' pointerEvents='none'>
                    <Icon fontSize='xl' as={iconLeft}></Icon>
                </InputLeftElement>
            }
            <Input py='4'isInvalid={isInvalid} {...props} {...field}></Input>
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

export default FormikInput
