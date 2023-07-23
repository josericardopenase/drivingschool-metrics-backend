import { Button, ButtonProps } from '@chakra-ui/react'
import { useFormikContext } from 'formik'
import React from 'react'

interface Props extends ButtonProps{}

function FormikButton(props: Props) {
    const formik = useFormikContext()
    return (
        <Button  onClick={() => formik.handleSubmit()} {...props} py='4'/>
    )
}

export default FormikButton