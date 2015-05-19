#define<stdio.h>

int main(int argc, char const *argv[])
{
	int t,n;
	scanf("%d\n",&t);
	while (t){
		scanf("%d\n",&n);
		int a[n],b[n];
		for (int i = 0; i < n; ++i)
		{
			printf("hello");
		}
		t=t-1;
	}
	return 0;
}


// def main():
// 	t = int(raw_input())
// 	c = []
// 	while t:
// 		n = int(raw_input())
// 		a = []
// 		b = []
// 		a = raw_input().split()
// 		for a_item in a:
// 			if a_item in b:
// 				pass
// 			else:
// 				b.append(a_item)
// 		t=t-1
// 		c.append(len(b))
// 	for values in c:
// 		print values
// main()