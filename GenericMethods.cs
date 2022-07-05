using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//C# project; 
//Reference: Curso Sololearn C #
//Under construction
 
namespace SoloLearn
{
 
    //Generic list 
    
    
    
    /* A list is similar to an array, but the elements in a list can be inserted and removed dynamically.
    The C# generic collection List<T> class requires all elements be of the same type T.
    */
    
    /*The System.Collections.Generic namespace includes the following generic collections:
    - List<T>
    - Dictionary<TKey, TValue>
    - SortedList<TKey, TValue>
    - Stack<T>
    - Queue<T>
    - Hashset<T>
    The System.Collections namespace includes the following non-generic collections: 
    - ArrayList
    - SortedList
    - Stack
    - Queue
    - Hashtable
    - BitArray
    */
    
    
    
    
    
    
    //Gewneric Dictionary & HashSet
    /* C# includes the HashSet<T> class in the generic collections namespace. All HashSet<T> elements are required to be of the same type T. 
    The HashSet<T> class provides high-performance set operations.
    HashSets allow fast lookup, addition, and removal of items, and can be used to implement either dynamic sets of items or lookup tables that allow finding an item by its key.
    (e.g., finding the phone number of a person by the last name).*/
    
        
    
    
        
    //Generic class - most commom use for generica classes is with collections of items.
    class Stack<T>{
     
        int index=0;
        T[] innerArray = new T[100];
        
        public void Push(T item){
            innerArray[index++]=item;
        }
        
        public T Pop(){
            return innerArray[--index];
        }
        
        public T Get(int k){return innerArray[k];}
    }
    
    // Generic provide a flexible mecanism to define a generic type.
    class Program
    {
        
        // Generic Methods
        static void Swap<T>(ref T a, ref T b){
            T temp = a;
            a = b;
            b = temp;
        }
        
        
        static void Main(string[] args)
        {
            
            //Generic List
            List<int> li = new List<int>();
            
            //Generic HashSet
            HashSet<int> hs = new HashSet<int>();
            
            
            Console.WriteLine("= = = = = = = = = = = = = = =");
            Console.WriteLine("C# - Generic Methods");
            Console.WriteLine(" ");
            Console.WriteLine("Example:");
            Console.WriteLine("static void Swap<T>(ref T a, ref T b){");
            Console.WriteLine("T temp = a; a = b; b = temp; }");
            Console.WriteLine(" ");
            
            //Gereric with int:
            int a = 4, b = 9;
            int c = a + b;
            Console.WriteLine("Generic method with int type:");
            Console.WriteLine("a:"+a+" b:"+b);
            Console.WriteLine("Swap");
            Swap<int>(ref a,ref b);
            Console.WriteLine("Int a:"+a+" + b:"+b+" = "+c);
            Console.WriteLine(" ");
            
            //Generic with double:
            Console.WriteLine("Generic method with double type:");
            double d = 4, e = 1.5;
            Console.WriteLine("Double - d:"+d+" e:"+e);
            Console.WriteLine("Swap()...");
            Swap<double>(ref d, ref e);
            Console.WriteLine("double - d:"+d+" e:"+e);
            
            //Generic Class:
            Console.WriteLine(" ");
            Console.WriteLine("= = = = = = = = = = = = = = =");
            Console.WriteLine("Generic Class");
            Console.WriteLine("Stack<int> intStack = new Stack<int>();");
            
            Console.WriteLine(" ");
            Stack<int> intStack = new Stack<int>();
            
            Console.WriteLine("Example:");
            
            Console.WriteLine("for (int x = 0; x <= 2; x++)");
            Console.WriteLine(" intStack.Push(x*2);");
            Console.WriteLine(" intStack{x} = intStack.Get(x)");
            Console.WriteLine(" ");
            for (int x = 0; x <= 2; x++)
            
            {
                intStack.Push(x*2);
                Console.WriteLine("intStack{"+x+"} = "+intStack.Get(x));
            }
            
        }
        
    }
    
}
