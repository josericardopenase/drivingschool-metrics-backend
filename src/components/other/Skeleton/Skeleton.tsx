import { SimpleGrid } from "@chakra-ui/react"
import { Skeleton } from "@chakra-ui/react"
import React from "react"

export interface SkeletonProps {
	cols?: number | number[]
	rows?: number
	height?: string
	spacing?: number
}

export default function BaseSkeleton({ cols = 1, rows = 5, height = "100px", spacing = 3 }: SkeletonProps) {
	return (
		<SimpleGrid columns={cols} spacing={spacing}>
			{[...Array(rows)].map((x1, i1) =>
				[...Array(cols)].map((x2, i2) => (
					<Skeleton
						borderRadius="xl"
						data-testid={"skeleton" + i1.toString() + i2.toString()}
						key={"skeleton" + i1.toString() + i2.toString()}
						height={height}
					/>
				))
			)}
		</SimpleGrid>
	)
}
