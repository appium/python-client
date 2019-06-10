#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver

from ..mobilecommand import MobileCommand as Command


class ImagesComparison(webdriver.Remote):

    def match_images_features(self, base64_image1, base64_image2, **opts):
        """Performs images matching by features.

        Read
        https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html
        for more details on this topic.
        The method supports all image formats, which are supported by OpenCV itself.

        Args:
            base64_image1 (bytes): base64-encoded content of the first image
            base64_image2 (bytes): base64-encoded content of the second image

        Keyword Args:
            visualize (bool): Set it to True in order to return the visualization of the matching operation.
                matching visualization. False by default
            detectorName (str): One of possible feature detector names:
                'AKAZE', 'AGAST', 'BRISK', 'FAST', 'GFTT', 'KAZE', 'MSER', 'SIFT', 'ORB'
                Some of these detectors are not enabled in the default OpenCV deployment.
                'ORB' By default.
            matchFunc (str): One of supported matching functions names:
                'FlannBased', 'BruteForce', 'BruteForceL1', 'BruteForceHamming',
                'BruteForceHammingLut', 'BruteForceSL2'
                'BruteForce' by default
            goodMatchesFactor (int): The maximum count of "good" matches (e. g. with minimal distances).
                This count is unlimited by default.

        Returns:
            The dictionary containing the following entries:

            visualization (bytes): base64-encoded content of PNG visualization of the current comparison
                operation. This entry is only present if `visualize` option is enabled
            count (int): The count of matched edges on both images.
                The more matching edges there are no both images the more similar they are.
            totalCount (int): The total count of matched edges on both images.
                It is equal to `count` if `goodMatchesFactor` does not limit the matches,
                otherwise it contains the total count of matches before `goodMatchesFactor` is
                applied.
            points1 (dict)): The array of matching points on the first image. Each point is a dictionary
                with 'x' and 'y' keys
            rect1 (dict): The bounding rect for the `points1` array or a zero rect if not enough matching points
                were found. The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
            points2 (dict): The array of matching points on the second image. Each point is a dictionary
                with 'x' and 'y' keys
            rect2 (dict): The bounding rect for the `points2` array or a zero rect if not enough matching points
                were found. The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
        """
        options = {
            'mode': 'matchFeatures',
            'firstImage': base64_image1,
            'secondImage': base64_image2,
            'options': opts
        }
        return self.execute(Command.COMPARE_IMAGES, options)['value']

    def find_image_occurrence(self, base64_full_image, base64_partial_image, **opts):
        """Performs images matching by template to find possible occurrence of the partial image
        in the full image.

        Read
        https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
        for more details on this topic.
        The method supports all image formats, which are supported by OpenCV itself.

        Args:
            base64_full_image (bytes): base64-encoded content of the full image
            base64_partial_image (bytes): base64-encoded content of the partial image

        Keyword Args:
            visualize (bool): Set it to True in order to return the visualization of the matching operation.
                False by default

        Returns:
            visualization (bytes): base64-encoded content of PNG visualization of the current comparison
                operation. This entry is only present if `visualize` option is enabled
            rect (dict): The region of the partial image occurrence on the full image.
                The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
        """
        options = {
            'mode': 'matchTemplate',
            'firstImage': base64_full_image,
            'secondImage': base64_partial_image,
            'options': opts
        }
        return self.execute(Command.COMPARE_IMAGES, options)['value']

    def get_images_similarity(self, base64_image1, base64_image2, **opts):
        """Performs images matching to calculate the similarity score between them.

        The flow there is similar to the one used in
        `find_image_occurrence`, but it is mandatory that both images are of equal resolution.
        The method supports all image formats, which are supported by OpenCV itself.

        Args:
            base64_image1 (bytes): base64-encoded content of the first image
            base64_image2 (bytes): base64-encoded content of the second image

        Keyword Args:
            visualize (bool): Set it to True in order to return the visualization of the matching operation.
                False by default

        Returns:
            visualization (bytes): base64-encoded content of PNG visualization of the current comparison
                operation. This entry is only present if `visualize` option is enabled
            score (float): The similarity score as a float number in range [0.0, 1.0].
                1.0 is the highest score (means both images are totally equal).
        """
        options = {
            'mode': 'getSimilarity',
            'firstImage': base64_image1,
            'secondImage': base64_image2,
            'options': opts
        }
        return self.execute(Command.COMPARE_IMAGES, options)['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.COMPARE_IMAGES] = \
            ('POST', '/session/$sessionId/appium/compare_images')
