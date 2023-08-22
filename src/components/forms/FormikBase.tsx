import { BoxProps, Flex, Icon, InputGroup, InputLeftElement, InputRightElement, Text } from '@chakra-ui/react'
import React from 'react'
import { FieldHelperProps, FieldInputProps, FieldMetaProps, useField } from 'formik';
import { IconType } from 'react-icons'

export interface FormikBaseProps extends Omit<BoxProps, 'children'> {
    name : string
    label ?: string
    iconLeft ?: IconType
    iconRight ?: IconType
    children : (field : FieldInputProps<any>, meta: FieldMetaProps<any>, helpers : FieldHelperProps<any>, props: BoxProps) => React.ReactNode
}

function FormikBase({name, label, iconLeft, iconRight, children, ...props}: FormikBaseProps) {
    const [field, meta, helpers] = useField(name);

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
            {
                children(field, meta, helpers, props)
            }
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

export default FormikBase
