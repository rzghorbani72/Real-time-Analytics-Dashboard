import { defineStore } from 'pinia'
import type { Metric } from '~/types/metric'

interface MetricsState {
  metrics: Metric[]
  loading: boolean
  error: string | null
}

export const useMetricsStore = defineStore('metrics', {
  state: (): MetricsState => ({
    metrics: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchMetrics() {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const response = await $fetch<Metric[]>(`${config.public.apiBase}/api/v1/metrics`)
        this.metrics = response
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to fetch metrics'
      } finally {
        this.loading = false
      }
    },

    async createMetric(metric: Omit<Metric, 'id' | 'timestamp'>) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const response = await $fetch<Metric>(`${config.public.apiBase}/api/v1/metrics`, {
          method: 'POST',
          body: metric
        })
        this.metrics.push(response)
        return response
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to create metric'
        throw error
      } finally {
        this.loading = false
      }
    }
  },

  getters: {
    metricsBySource: (state) => {
      return (source: string) => state.metrics.filter(m => m.source === source)
    }
  }
})

