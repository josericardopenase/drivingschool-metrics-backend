import React from "react"
import { ComponentMeta } from "@storybook/react"
import Skeleton from "./Skeleton"

// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
	title: "components/other/Skeleton",
	component: Skeleton,
	// More on argTypes: https://storybook.js.org/docs/react/api/argtypes
} as ComponentMeta<typeof Skeleton>

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args

export const Primary = () => <Skeleton></Skeleton>
