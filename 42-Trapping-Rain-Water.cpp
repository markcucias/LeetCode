class Solution {
public:
    int find_water(std::vector<int>& height, int index) {
        int water = 0;
        int max = 0;

        for (size_t i = 0; i < index; i++) {
            if (std::min(max, height[index]) - height[i] > 0) {
                water += std::min(max, height[index]) - height[i];
            }
            if (height[i] > max) max = height[i];
        }

        max = 0;
        for (size_t i = height.size() - 1; i > index; i--) {
            if (std::min(max, height[index]) - height[i] > 0) {
                water += std::min(max, height[index]) - height[i];
            }
            if (height[i] > max) max = height[i];
        }

        return water;
    }

    int trap(std::vector<int>& height) {
        int max = 0;
        for (int i = 0; i < height.size(); i++) {
            if (height[i] > height[max]) max = i;
        }

        return find_water(height, max);
    }

};