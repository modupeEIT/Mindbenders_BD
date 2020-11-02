package ASS1

import scala.io.Source

object wordcount {
  def main(args:Array[String]): Unit ={

    val s1 = List(Source.fromFile("Shakespeare.txt").mkString);
    val s2 = s1.map(lines => lines.toLowerCase())
    val words = s2.flatMap(line => line.split("\\W+"))
    val keyData = words.map(word => (word,1))
    val groupedData = keyData.groupBy(_._1)
    val result = groupedData.view.mapValues(list=>{
    list.map(_._2).sum
    })
    result.foreach(println)
  }
}
