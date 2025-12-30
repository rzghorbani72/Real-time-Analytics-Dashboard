<template>
  <div>
    <h2 class="text-xl font-semibold mb-4">Dashboard Overview</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-lg font-medium mb-2">Metrics</h3>
        <p class="text-gray-600">View and manage metrics</p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-lg font-medium mb-2">Dashboards</h3>
        <p class="text-gray-600">Create custom dashboards</p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-lg font-medium mb-2">Visualizations</h3>
        <p class="text-gray-600">Interactive D3 charts</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: 'Home'
})
</script>

