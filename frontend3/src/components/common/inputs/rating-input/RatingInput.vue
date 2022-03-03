<template>
  <div class="flex flex-row">
    <Star @mouseover="changeHoverRating(1)" @mouseleave="changeHoverRating(rating)" @click="selected=true; rating=1" class="star" :filled="hoverRating>=1"/>
    <Star @mouseover="changeHoverRating(2)" @mouseleave="changeHoverRating(rating)" @click="selected=true; rating=2" class="star" :filled="hoverRating>=2"/>
    <Star @mouseover="changeHoverRating(3)" @mouseleave="changeHoverRating(rating)" @click="selected=true; rating=3" class="star" :filled="hoverRating>=3"/>
    <Star @mouseover="changeHoverRating(4)" @mouseleave="changeHoverRating(rating)" @click="selected=true; rating=4" class="star" :filled="hoverRating>=4"/>
    <Star @mouseover="changeHoverRating(5)" @mouseleave="changeHoverRating(rating)" @click="selected=true; rating=5" class="star" :filled="hoverRating>=5"/>
    <span>{{hoverRating}} {{rating}} {{selected}}</span>
  </div>
</template>

<script>
import Star from "./Star";

export default {
  name: "RatingInput",
  components: {
    Star
  },
  data(){
    return{
      rating: 0,
      hoverRating: 0,
      selected: false
    }
  },
  methods: {
    changeHoverRating(newRating) {
        this.hoverRating = newRating;
    }
  }
}
</script>

<style scoped>

</style>