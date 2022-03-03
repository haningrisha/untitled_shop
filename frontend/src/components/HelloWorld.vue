<template>
  <div>
    <DropDown></DropDown>
  </div>
</template>

<script>
import DropDown from "@/components/common/inputs/DropDown";

export default {
  name: "HelloWorld",
  components: {
    DropDown
  },
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
