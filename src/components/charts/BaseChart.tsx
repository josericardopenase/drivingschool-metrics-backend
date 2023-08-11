import { Box , Text} from '@chakra-ui/react'
import { Formik } from 'formik'
import React, { useState } from 'react'

interface Props {
    setFilters:  any,
    filtersValue : any,
    filters : React.ReactNode,
    children : React.ReactNode
    title: string
}

function BaseChart(props: Props) {

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
        <Box bgColor='white' p='6' borderRadius='3xl'>
            <Text fontSize='lg' fontWeight='semibold'>{props.title}</Text>
            {
                props.filters && 
                <Formik validateOnBlur={true} validateOnChange={true} validate={handle} initialValues={props.filtersValue ?? {}} onSubmit={() => {}}>
                    {
                        props.filters
                    }
                </Formik>
            }
            <Box w='100%' p='5'>
            {
                props.children
            }
            </Box>
        </Box>
        
    )
}

export default BaseChart
