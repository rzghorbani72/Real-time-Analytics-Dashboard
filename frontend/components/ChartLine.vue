<template>
  <div ref="chartContainer" class="w-full h-64"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as d3 from 'd3'

interface Props {
  data: Array<{ timestamp: string; value: number }>
  width?: number
  height?: number
}

const props = withDefaults(defineProps<Props>(), {
  width: 800,
  height: 400
})

const chartContainer = ref<HTMLElement | null>(null)

const drawChart = () => {
  if (!chartContainer.value || !props.data.length) return

  d3.select(chartContainer.value).selectAll('*').remove()

  const margin = { top: 20, right: 20, bottom: 40, left: 50 }
  const width = props.width - margin.left - margin.right
  const height = props.height - margin.top - margin.bottom

  const svg = d3.select(chartContainer.value)
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)

  const g = svg.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  const x = d3.scaleTime()
    .domain(d3.extent(props.data, d => new Date(d.timestamp)) as [Date, Date])
    .range([0, width])

  const y = d3.scaleLinear()
    .domain(d3.extent(props.data, d => d.value) as [number, number])
    .nice()
    .range([height, 0])

  const line = d3.line<{ timestamp: string; value: number }>()
    .x(d => x(new Date(d.timestamp)))
    .y(d => y(d.value))
    .curve(d3.curveMonotoneX)

  g.append('g')
    .attr('transform', `translate(0,${height})`)
    .call(d3.axisBottom(x))

  g.append('g')
    .call(d3.axisLeft(y))

  g.append('path')
    .datum(props.data)
    .attr('fill', 'none')
    .attr('stroke', 'steelblue')
    .attr('stroke-width', 2)
    .attr('d', line)
}

onMounted(() => {
  drawChart()
})

watch(() => props.data, () => {
  drawChart()
}, { deep: true })
</script>

