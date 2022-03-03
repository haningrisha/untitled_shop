<template>
  <div v-if="filled">
    <StarIconSolid class="star"/>
  </div>
  <div v-else>
    <StarIconOutline class="star"/>
  </div>
</template>

<script>
import { StarIcon as StarIconOutline } from "@heroicons/vue/outline"
import { StarIcon as StarIconSolid } from "@heroicons/vue/solid"

export default {
  name: "Star",
  props: {
    filled: Boolean
  },
  components: {
    StarIconOutline,
    StarIconSolid
  }
}
</script>

<style scoped>
.star {
  @apply w-5 h-5 text-black
}
</style>