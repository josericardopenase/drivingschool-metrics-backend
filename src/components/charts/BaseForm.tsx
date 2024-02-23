import { Box , Text} from '@chakra-ui/react'
import { Formik } from 'formik'
import React, { useState } from 'react'

interface Props {
    setFilters:  any,
    filtersValue : any,
    filters : React.ReactNode,
    children : React.ReactNode
}

function BaseForm(props: Props) {

    const [insideFilters, setInsideFilters] = useState({})
	const [timer, setTimer] = useState<any>(null);
    
	function handle(values: any) {
		setInsideFilters(values);

		if (timer) clearTimeout(timer);

		const newTimer = setTimeout(() => {
			props.setFilters(values);
		}, 500);

		setTimer(newTimer);
	}


    return (
        <>
            {
                props.filters && 
                <Formik validateOnBlur={true} validateOnChange={true} validate={handle} initialValues={props.filtersValue ?? {}} onSubmit={() => {}}>
                    {
                        props.filters
                    }
                </Formik>
            }
            <Box w='100%' p='0'>
            {
                props.children
            }
            </Box>
        </>
    )
}

export default BaseForm
