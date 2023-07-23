import React from 'react'
import useLogout from '../../../api/auth/useLogout'

interface Props {}

function Metrics(props: Props) {

    const {mutate} = useLogout()

    return (
        <div onClick={() => mutate()}>Metrics</div>
    )
}
export default Metrics
