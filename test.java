import java.util.*;

public class J_2606 {
    static boolean[] check = new boolean[101]; //방문한 노드인지 체킹
    static int[][] graph = new int[101][101]; //인접노드
    static int n; //컴퓨터 개수
    static int cnt = 0; //바이러스 컴퓨터 개수

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        cnt = scanner.nextInt();
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < cnt + 1; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph[a][b] = graph[b][a] = 1; //그래프 생성
        }
        bfs(1);
        System.out.println(cnt);
    }

    public static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        check[start] = true; //시작노드 1
        queue.offer(start);

        while (!queue.isEmpty()) {
            int tmp = queue.poll();
            for (int i = 1; i <= n; i++) {
                if ((graph[tmp][i]) == 1 && check[i] == false) {
                    cnt++;
                    queue.add(i);
                    check[i] = true;
                }
            }
        }

    }
}