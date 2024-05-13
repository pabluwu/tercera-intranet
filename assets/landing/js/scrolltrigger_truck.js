const photos = gsap.utils.toArray(".truck_photo:not(:first-child)");

gsap.set(photos, {yPercent: 101})

const animation = gsap.to( photos, {
    yPercent:0,
    duration:1,
    stagger:1,
})

let mm = gsap.matchMedia();

mm.add("(min-width: 600px)", ()=>{

    ScrollTrigger.create({
        trigger: ".gallery",
        markers:false,
        start: "0%",
        end : "bottom bottom",
        pin : ".left",
        animation:animation,
        scrub:true,
        
    })
})
