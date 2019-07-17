
import java.util.HashMap; 

class Node
{
	int key;
	int value;
	Node prev;
	Node next;
	public Node(int key, int value)
	{
		this.key = key;
		this.value = value;
	}
}

class LRUCache 
{
	int capacity;
	HashMap<Integer, Node> map = new HashMap<Integer, Node>();
	Node head=null;
	Node end=null;
	public LRUCache(int capacity) 
	{
		this.capacity = capacity;
	}

	//get item from LRU cache 
	public int getItem(int key) 
	{
		if(map.containsKey(key))
		{
			Node n = map.get(key);
			deletenode(n);
			setHead(n);
			return n.value;
		}
		return -1;
	}
 
	// deletenode one node
	public void deletenode(Node node)
	{
		if(node.prev!=null)
		{
			node.prev.next = node.next;
		}
		else
		{
			head = node.next;
		}
		if(node.next!=null)
		{
			node.next.prev = node.prev;
		}
		else
		{
			end = node.prev;
		}
 
	}
 
	// make node as head node
	public void setHead(Node node)
	{
		node.next = head;
		node.prev = null;
		if(head!=null)
		{
			head.prev = node;
		}
		head = node;
		if(end ==null)
		{
			end = head;
		}
	}

 	//set item in LRU cache 
	public void setItem(int key, int value) 
	{
		if(map.containsKey(key))
		{
			// update the old value
			Node old = map.get(key);
			old.value = value;
			deletenode(old);
			setHead(old);
		}
		else
		{
			Node newNode = new Node(key, value);
			if(map.size()>=capacity)
			{
				map.remove(end.key);
				// remove last node
				deletenode(end);
				setHead(newNode);
 			}
			else
			{
				setHead(newNode);
			}    
			map.put(key, newNode);
		}
	}	
	
	public static void main(String[] args) throws java.lang.Exception 
	{
		LRUCache lrucache = new LRUCache(4);
		lrucache.setItem(1, 100);
		lrucache.setItem(10, 99);
		lrucache.setItem(15, 98);
		lrucache.setItem(10, 97);
		lrucache.setItem(12, 96);
		lrucache.setItem(18, 95);
		lrucache.setItem(1, 94);
		System.out.println(lrucache.getItem(1));
		System.out.println(lrucache.getItem(10));
		System.out.println(lrucache.getItem(15));
	}
}