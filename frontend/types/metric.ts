export interface Metric {
  id: number
  name: string
  value: number
  timestamp: string
  source?: string
}

export interface MetricCreate {
  name: string
  value: number
  source?: string
}

