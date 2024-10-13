fun main(args: Array<String>) {
   val titam = Rocket()
   titam.toFuel(1000.0)
   titam.start()
    
}

class Rocket(){
   var power: Double = 0.0
   var tank: Double = 0.0
   var efficiency: Double  = 1.02
   var fluxo: Double = 5.0

   
   fun toFuel(x: Double){
       print("Fuel;")
       this.tank = this.tank + x
       println(x)
   }
   
  
   fun start(){
       println("Rocket launch!")
       println("Fuel - Power:")
       while (this.tank > 0.0){
       this.power = (this.power +1)* this.efficiency 
       this.tank= this.tank - this.fluxo 
       print(this.tank)     
       println(" - "+this.power)
       
       }
       println("Fuel off!")
   }  
   
        }
