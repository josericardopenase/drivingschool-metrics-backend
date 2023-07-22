import React from 'react'

interface Props {}

function Metrics(props: Props) {
    return (
        <div onClick={() => localStorage.setItem('token', '')}>Metrics</div>
    )
}
export default Metrics
