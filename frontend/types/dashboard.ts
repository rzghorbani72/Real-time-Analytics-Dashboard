export interface Dashboard {
  id: number
  name: string
  description?: string
  config: Record<string, any>
  created_at: string
  updated_at?: string
}

export interface DashboardCreate {
  name: string
  description?: string
  config: Record<string, any>
}

