import React from "react"
import { render, screen } from "@testing-library/react"
import Skeleton from "./Skeleton"

describe("UI testing", () => {
	test("The component has not render correctly", () => {
		render(<Skeleton />)
	})
	test("The component must set the rows using rows prop", () => {
		render(<Skeleton rows={3} />)
		screen.getByTestId("skeleton20")
		screen.getByTestId("skeleton10")
		screen.getByTestId("skeleton00")
	})
	test("The component must set the cols using cols prop", () => {
		render(<Skeleton cols={3} />)
		screen.getByTestId("skeleton00")
		screen.getByTestId("skeleton01")
		screen.getByTestId("skeleton02")
	})

	test("The component must set the cols using cols prop", () => {
		render(<Skeleton cols={2} rows={2} />)
		screen.getByTestId("skeleton00")
		screen.getByTestId("skeleton01")
		screen.getByTestId("skeleton10")
		screen.getByTestId("skeleton11")
	})
})
