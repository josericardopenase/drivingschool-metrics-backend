import React, { useState } from "react";
import { Formik } from "formik";

interface props {
	setFilters: React.Dispatch<React.SetStateAction<any>>;
	setLoading: React.Dispatch<React.SetStateAction<boolean>>;
	initialValues?: any;
	children: React.ReactNode;
}

export default function FormikFilters({
	setFilters,
	setLoading,
	children,
	initialValues = {},
}: props) {
	const [insideFilters, setInsideFilters] = useState<unknown>(initialValues);
	const [timer, setTimer] = useState<any>(null);

	function handle(values: any) {
		setLoading(true);
		setInsideFilters(values);

		if (timer) clearTimeout(timer);

		const newTimer = setTimeout(() => {
			setFilters(values);
			setLoading(false);
		}, 500);

		setTimer(newTimer);
	}

	return (
		<Formik
			initialValues={{ ...initialValues }}
			validateOnChange={true}
			validate={handle}
			onSubmit={(values, helpers) => {
				handle(values);
				helpers.setSubmitting(false);
			}}
		>
			{() => <div style={{ width: "100%" }}>{children}</div>}
		</Formik>
	);
}
