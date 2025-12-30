import { defineStore } from 'pinia'
import type { Dashboard } from '~/types/dashboard'

interface DashboardsState {
  dashboards: Dashboard[]
  loading: boolean
  error: string | null
}

export const useDashboardsStore = defineStore('dashboards', {
  state: (): DashboardsState => ({
    dashboards: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchDashboards() {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const response = await $fetch<Dashboard[]>(`${config.public.apiBase}/api/v1/dashboards`)
        this.dashboards = response
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to fetch dashboards'
      } finally {
        this.loading = false
      }
    },

    async createDashboard(dashboard: Omit<Dashboard, 'id' | 'created_at' | 'updated_at'>) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const response = await $fetch<Dashboard>(`${config.public.apiBase}/api/v1/dashboards`, {
          method: 'POST',
          body: dashboard
        })
        this.dashboards.push(response)
        return response
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to create dashboard'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})

