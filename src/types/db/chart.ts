export interface Chart{
    info : {
        x_label: string,
        y_labels: string[]
    }
    records: Record<string, any>[]
}